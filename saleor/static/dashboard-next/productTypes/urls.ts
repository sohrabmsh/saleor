import { stringify as stringifyQs } from "qs";
import * as urlJoin from "url-join";

import { Dialog, SingleAction } from "../types";
import { AttributeTypeEnum } from "../types/globalTypes";

const productTypeSection = "/product-types/";

export const productTypeListPath = productTypeSection;
export const productTypeListUrl = productTypeListPath;

export const productTypeAddPath = urlJoin(productTypeSection, "add");
export const productTypeAddUrl = productTypeAddPath;

export const productTypePath = (id: string) => urlJoin(productTypeSection, id);
export type ProductTypeUrlDialog =
  | "add-attribute"
  | "edit-attribute"
  | "remove";
export type ProductTypeUrlQueryParams = Dialog<ProductTypeUrlDialog> &
  SingleAction & {
    type?: AttributeTypeEnum;
  };
export const productTypeUrl = (
  id: string,
  params?: ProductTypeUrlQueryParams
) => productTypePath(encodeURIComponent(id)) + "?" + stringifyQs(params);

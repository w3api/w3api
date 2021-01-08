---
title: CatalogResolver
permalink: Java/CatalogResolver
date: 2021-01-04
key: JavaJava.C.CatalogResolver
category: java
tags: ['java se', 'javax.xml.catalog', 'java.xml', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CatalogResolver.description }}

## Sintaxis
~~~java
public interface CatalogResolver extends EntityResolver, XMLResolver, URIResolver, LSResourceResolver
~~~

## Métodos
* [resolve()](/Java/CatalogResolver/resolve)
* [resolveEntity()](/Java/CatalogResolver/resolveEntity)
* [resolveResource()](/Java/CatalogResolver/resolveResource)

## Ejemplo
~~~java
{{ site.data.Java.C.CatalogResolver.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CatalogResolver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

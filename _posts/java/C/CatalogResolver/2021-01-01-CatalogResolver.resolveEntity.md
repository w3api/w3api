---
title: CatalogResolver.resolveEntity()
permalink: /Java/CatalogResolver/resolveEntity/
date: 2021-01-11
key: Java.C.CatalogResolver
category: Java
tags: ['java se', 'javax.xml.catalog', 'java.xml', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CatalogResolver.metodos valor="resolveEntity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
InputSource resolveEntity(String publicId, String systemId)
InputStream resolveEntity(String publicId, String systemId, String baseUri, String namespace)
~~~

## Parámetros
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **String namespace**,  {% include w3api/param_description.html metodo=_dato parametro="String namespace" %}
* **String baseUri**,  {% include w3api/param_description.html metodo=_dato parametro="String baseUri" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_dato parametro="String publicId" %}

## Excepciones
[CatalogException](/Java/CatalogException/)

## Clase Padre
[CatalogResolver](/Java/CatalogResolver/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

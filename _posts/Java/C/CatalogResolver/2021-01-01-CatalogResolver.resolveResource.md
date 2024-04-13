---
title: CatalogResolver.resolveResource()
permalink: /Java/CatalogResolver/resolveResource/
date: 2021-01-11
key: Java.C.CatalogResolver
category: Java
tags: ['java se', 'javax.xml.catalog', 'java.xml', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CatalogResolver.metodos valor="resolveResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LSInput resolveResource(String type, String namespaceUri, String publicId, String systemId, String baseUri)
~~~

## Parámetros
* **String namespaceUri**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceUri" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
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

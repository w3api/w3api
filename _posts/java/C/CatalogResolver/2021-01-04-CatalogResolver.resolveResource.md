---
title: CatalogResolver.resolveResource()
permalink: Java/CatalogResolver/resolveResource
date: 2021-01-04
key: JavaJava.C.CatalogResolver
category: java
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
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **String baseUri**,  {% include w3api/param_description.html metodo=_data parametro="String baseUri" %}
* **String namespaceUri**,  {% include w3api/param_description.html metodo=_data parametro="String namespaceUri" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_data parametro="String publicId" %}

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
{%- for _ldc in site.data.Java.C.CatalogResolver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

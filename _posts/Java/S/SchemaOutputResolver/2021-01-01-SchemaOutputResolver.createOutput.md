---
title: SchemaOutputResolver.createOutput()
permalink: /Java/SchemaOutputResolver/createOutput/
date: 2021-01-11
key: Java.S.SchemaOutputResolver
category: Java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SchemaOutputResolver.metodos valor="createOutput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Result createOutput(String namespaceUri, String suggestedFileName) throws IOException
~~~

## Parámetros
* **String namespaceUri**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceUri" %}
* **String suggestedFileName**,  {% include w3api/param_description.html metodo=_dato parametro="String suggestedFileName" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[SchemaOutputResolver](/Java/SchemaOutputResolver/)

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

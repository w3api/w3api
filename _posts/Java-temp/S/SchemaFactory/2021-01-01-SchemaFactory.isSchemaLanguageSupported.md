---
title: SchemaFactory.isSchemaLanguageSupported()
permalink: /Java/SchemaFactory/isSchemaLanguageSupported/
date: 2021-01-11
key: Java.S.SchemaFactory
category: Java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SchemaFactory.metodos valor="isSchemaLanguageSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean isSchemaLanguageSupported(String schemaLanguage)
~~~

## Parámetros
* **String schemaLanguage**,  {% include w3api/param_description.html metodo=_dato parametro="String schemaLanguage" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SchemaFactory](/Java/SchemaFactory/)

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

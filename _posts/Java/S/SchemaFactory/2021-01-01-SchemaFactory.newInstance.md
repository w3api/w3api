---
title: SchemaFactory.newInstance()
permalink: /Java/SchemaFactory/newInstance/
date: 2021-01-11
key: Java.S.SchemaFactory
category: Java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SchemaFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SchemaFactory newInstance(String schemaLanguage)
public static SchemaFactory newInstance(String schemaLanguage, String factoryClassName, ClassLoader classLoader)
~~~

## Parámetros
* **String schemaLanguage**,  {% include w3api/param_description.html metodo=_dato parametro="String schemaLanguage" %}
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}
* **String factoryClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String factoryClassName" %}

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

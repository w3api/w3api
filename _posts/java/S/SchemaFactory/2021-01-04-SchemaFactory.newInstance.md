---
title: SchemaFactory.newInstance()
permalink: Java/SchemaFactory/newInstance
date: 2021-01-04
key: JavaJava.S.SchemaFactory
category: java
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
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader classLoader" %}
* **String schemaLanguage**,  {% include w3api/param_description.html metodo=_data parametro="String schemaLanguage" %}
* **String factoryClassName**,  {% include w3api/param_description.html metodo=_data parametro="String factoryClassName" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SchemaFactory](/Java/SchemaFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SchemaFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

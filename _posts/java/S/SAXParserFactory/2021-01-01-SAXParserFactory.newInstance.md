---
title: SAXParserFactory.newInstance()
permalink: /Java/SAXParserFactory/newInstance/
date: 2021-01-11
key: Java.S.SAXParserFactory
category: Java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAXParserFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SAXParserFactory newInstance()
public static SAXParserFactory newInstance(String factoryClassName, ClassLoader classLoader)
~~~

## Parámetros
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}
* **String factoryClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String factoryClassName" %}

## Clase Padre
[SAXParserFactory](/Java/SAXParserFactory/)

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

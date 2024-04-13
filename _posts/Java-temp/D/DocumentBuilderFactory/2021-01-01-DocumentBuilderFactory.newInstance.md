---
title: DocumentBuilderFactory.newInstance()
permalink: /Java/DocumentBuilderFactory/newInstance/
date: 2021-01-11
key: Java.D.DocumentBuilderFactory
category: Java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentBuilderFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DocumentBuilderFactory newInstance()
public static DocumentBuilderFactory newInstance(String factoryClassName, ClassLoader classLoader)
~~~

## Parámetros
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}
* **String factoryClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String factoryClassName" %}

## Clase Padre
[DocumentBuilderFactory](/Java/DocumentBuilderFactory/)

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

---
title: Attributes2Impl.isDeclared()
permalink: Java/Attributes2Impl/isDeclared
date: 2021-01-11
key: JavaJava.A.Attributes2Impl
category: java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.5', 'SAX 2.0 (extensions Java 1.1 alpha)']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attributes2Impl.metodos valor="isDeclared" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isDeclared(int index)
public boolean isDeclared(String qName)
public boolean isDeclared(String uri, String localName)
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String qName**,  {% include w3api/param_description.html metodo=_dato parametro="String qName" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}

## Clase Padre
[Attributes2Impl](/Java/Attributes2Impl/)

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

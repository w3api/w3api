---
title: MimeHeaders.addHeader()
permalink: Java/MimeHeaders/addHeader
date: 2021-01-11
key: JavaJava.M.MimeHeaders
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MimeHeaders.metodos valor="addHeader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addHeader(String name, String value)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MimeHeaders](/Java/MimeHeaders/)

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

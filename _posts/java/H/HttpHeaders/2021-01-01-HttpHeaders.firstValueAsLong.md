---
title: HttpHeaders.firstValueAsLong()
permalink: /Java/HttpHeaders/firstValueAsLong/
date: 2021-01-11
key: Java.H.HttpHeaders
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpHeaders.metodos valor="firstValueAsLong" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OptionalLong firstValueAsLong(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[NumberFormatException](/Java/NumberFormatException/)

## Clase Padre
[HttpHeaders](/Java/HttpHeaders/)

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

---
title: SocketOptions.setOption()
permalink: Java/SocketOptions/setOption
date: 2021-01-04
key: JavaJava.S.SocketOptions
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketOptions.metodos valor="setOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setOption(int optID, Object value) throws SocketException
~~~

## Parámetros
* **int optID**,  {% include w3api/param_description.html metodo=_data parametro="int optID" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Excepciones
[SocketException](/Java/SocketException/)

## Clase Padre
[SocketOptions](/Java/SocketOptions/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SocketOptions.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

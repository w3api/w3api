---
title: SocketOptions.setOption()
permalink: /Java/SocketOptions/setOption/
date: 2021-01-11
key: Java.S.SocketOptions
category: Java
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
* **int optID**,  {% include w3api/param_description.html metodo=_dato parametro="int optID" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

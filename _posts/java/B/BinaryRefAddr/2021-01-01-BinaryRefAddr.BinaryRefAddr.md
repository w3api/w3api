---
title: BinaryRefAddr.BinaryRefAddr()
permalink: /Java/BinaryRefAddr/BinaryRefAddr/
date: 2021-01-11
key: Java.B.BinaryRefAddr
category: Java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BinaryRefAddr.constructores valor="BinaryRefAddr" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BinaryRefAddr(String addrType, byte[] src)
public BinaryRefAddr(String addrType, byte[] src, int offset, int count)
~~~

## Parámetros
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}
* **byte[] src**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] src" %}
* **String addrType**,  {% include w3api/param_description.html metodo=_dato parametro="String addrType" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Clase Padre
[BinaryRefAddr](/Java/BinaryRefAddr/)

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

---
title: DatagramPacket.setData()
permalink: Java/DatagramPacket/setData
date: 2021-01-11
key: JavaJava.D.DatagramPacket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramPacket.metodos valor="setData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setData(byte[] buf)
public void setData(byte[] buf, int offset, int length)
~~~

## Parámetros
* **byte[] buf**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] buf" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DatagramPacket](/Java/DatagramPacket/)

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

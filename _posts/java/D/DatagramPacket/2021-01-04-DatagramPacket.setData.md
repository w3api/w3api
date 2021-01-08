---
title: DatagramPacket.setData()
permalink: Java/DatagramPacket/setData
date: 2021-01-04
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
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **byte[] buf**,  {% include w3api/param_description.html metodo=_data parametro="byte[] buf" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

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
{%- for _ldc in site.data.Java.D.DatagramPacket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: DatagramPacket.setSocketAddress()
permalink: /Java/DatagramPacket/setSocketAddress/
date: 2021-01-11
key: Java.D.DatagramPacket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramPacket.metodos valor="setSocketAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSocketAddress(SocketAddress address)
~~~

## Parámetros
* **SocketAddress address**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress address" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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

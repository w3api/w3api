---
title: DatagramSocketImpl.peekData()
permalink: /Java/DatagramSocketImpl/peekData/
date: 2021-01-11
key: Java.D.DatagramSocketImpl
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocketImpl.metodos valor="peekData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract int peekData(DatagramPacket p) throws IOException
~~~

## Parámetros
* **DatagramPacket p**,  {% include w3api/param_description.html metodo=_dato parametro="DatagramPacket p" %}

## Excepciones
[PortUnreachableException](/Java/PortUnreachableException/), [IOException](/Java/IOException/)

## Clase Padre
[DatagramSocketImpl](/Java/DatagramSocketImpl/)

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

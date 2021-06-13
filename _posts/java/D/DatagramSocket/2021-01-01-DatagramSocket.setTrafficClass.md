---
title: DatagramSocket.setTrafficClass()
permalink: /Java/DatagramSocket/setTrafficClass/
date: 2021-01-11
key: Java.D.DatagramSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocket.metodos valor="setTrafficClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTrafficClass(int tc) throws SocketException
~~~

## Parámetros
* **int tc**,  {% include w3api/param_description.html metodo=_dato parametro="int tc" %}

## Excepciones
[SocketException](/Java/SocketException/)

## Clase Padre
[DatagramSocket](/Java/DatagramSocket/)

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

---
title: SocketImpl.sendUrgentData()
permalink: Java/SocketImpl/sendUrgentData
date: 2021-01-04
key: JavaJava.S.SocketImpl
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SocketImpl.metodos valor="sendUrgentData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void sendUrgentData(int data) throws IOException
~~~

## Parámetros
* **int data**,  {% include w3api/param_description.html metodo=_data parametro="int data" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[SocketImpl](/Java/SocketImpl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SocketImpl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

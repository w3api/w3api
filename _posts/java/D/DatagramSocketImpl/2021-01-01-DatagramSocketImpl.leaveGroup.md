---
title: DatagramSocketImpl.leaveGroup()
permalink: /Java/DatagramSocketImpl/leaveGroup/
date: 2021-01-11
key: Java.D.DatagramSocketImpl
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocketImpl.metodos valor="leaveGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void leaveGroup(SocketAddress mcastaddr, NetworkInterface netIf) throws IOException
~~~

## Parámetros
* **SocketAddress mcastaddr**,  {% include w3api/param_description.html metodo=_dato parametro="SocketAddress mcastaddr" %}
* **NetworkInterface netIf**,  {% include w3api/param_description.html metodo=_dato parametro="NetworkInterface netIf" %}

## Excepciones
[IOException](/Java/IOException/)

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

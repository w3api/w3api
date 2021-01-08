---
title: DatagramSocketImpl.bind()
permalink: Java/DatagramSocketImpl/bind
date: 2021-01-04
key: JavaJava.D.DatagramSocketImpl
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocketImpl.metodos valor="bind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void bind(int lport, InetAddress laddr) throws SocketException
~~~

## Parámetros
* **InetAddress laddr**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress laddr" %}
* **int lport**,  {% include w3api/param_description.html metodo=_data parametro="int lport" %}

## Excepciones
[SocketException](/Java/SocketException/)

## Clase Padre
[DatagramSocketImpl](/Java/DatagramSocketImpl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatagramSocketImpl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

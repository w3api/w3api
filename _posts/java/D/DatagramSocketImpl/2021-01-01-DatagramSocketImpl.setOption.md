---
title: DatagramSocketImpl.setOption()
permalink: /Java/DatagramSocketImpl/setOption/
date: 2021-01-11
key: Java.D.DatagramSocketImpl
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatagramSocketImpl.metodos valor="setOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected <T> void setOption(SocketOption<T> name, T value)
~~~

## Parámetros
* **SocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_dato parametro="SocketOption<T> name" %}
* **T value**,  {% include w3api/param_description.html metodo=_dato parametro="T value" %}

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

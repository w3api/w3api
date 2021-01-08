---
title: DatagramSocketImpl.setOption()
permalink: Java/DatagramSocketImpl/setOption
date: 2021-01-04
key: JavaJava.D.DatagramSocketImpl
category: java
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
* **T value**,  {% include w3api/param_description.html metodo=_data parametro="T value" %}
* **SocketOption&lt;T&gt; name**,  {% include w3api/param_description.html metodo=_data parametro="SocketOption<T> name" %}

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

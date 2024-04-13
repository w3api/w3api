---
title: ChannelBinding.ChannelBinding()
permalink: /Java/ChannelBinding/ChannelBinding/
date: 2021-01-11
key: Java.C.ChannelBinding
category: Java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChannelBinding.constructores valor="ChannelBinding" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ChannelBinding(byte[] appData)
public ChannelBinding(InetAddress initAddr, InetAddress acceptAddr, byte[] appData)
~~~

## Parámetros
* **byte[] appData**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] appData" %}
* **InetAddress initAddr**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress initAddr" %}
* **InetAddress acceptAddr**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress acceptAddr" %}

## Clase Padre
[ChannelBinding](/Java/ChannelBinding/)

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

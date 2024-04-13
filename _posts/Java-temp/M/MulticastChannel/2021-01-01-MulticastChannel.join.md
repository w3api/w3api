---
title: MulticastChannel.join()
permalink: /Java/MulticastChannel/join/
date: 2021-01-11
key: Java.M.MulticastChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MulticastChannel.metodos valor="join" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
MembershipKey join(InetAddress group, NetworkInterface interf) throws IOException
MembershipKey join(InetAddress group, NetworkInterface interf, InetAddress source) throws IOException
~~~

## Parámetros
* **InetAddress group**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress group" %}
* **InetAddress source**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress source" %}
* **NetworkInterface interf**,  {% include w3api/param_description.html metodo=_dato parametro="NetworkInterface interf" %}

## Excepciones
[ClosedChannelException](/Java/ClosedChannelException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[MulticastChannel](/Java/MulticastChannel/)

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

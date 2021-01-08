---
title: MulticastChannel.join()
permalink: Java/MulticastChannel/join
date: 2021-01-04
key: JavaJava.M.MulticastChannel
category: java
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
* **NetworkInterface interf**,  {% include w3api/param_description.html metodo=_data parametro="NetworkInterface interf" %}
* **InetAddress group**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress group" %}
* **InetAddress source**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress source" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/), [ClosedChannelException](/Java/ClosedChannelException/), [IOException](/Java/IOException/)

## Clase Padre
[MulticastChannel](/Java/MulticastChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MulticastChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

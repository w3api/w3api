---
title: InterruptibleChannel.close()
permalink: /Java/InterruptibleChannel/close/
date: 2021-01-11
key: Java.I.InterruptibleChannel
category: Java
tags: ['java se', 'java.nio.channels', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InterruptibleChannel.metodos valor="close" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void close() throws IOException
~~~

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[InterruptibleChannel](/Java/InterruptibleChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

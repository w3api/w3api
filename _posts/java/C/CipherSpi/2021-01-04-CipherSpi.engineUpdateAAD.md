---
title: CipherSpi.engineUpdateAAD()
permalink: Java/CipherSpi/engineUpdateAAD
date: 2021-01-04
key: JavaJava.C.CipherSpi
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherSpi.metodos valor="engineUpdateAAD" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void engineUpdateAAD(byte[] src, int offset, int len)
protected void engineUpdateAAD(ByteBuffer src)
~~~

## Parámetros
* **byte[] src**,  {% include w3api/param_description.html metodo=_data parametro="byte[] src" %}
* **ByteBuffer src**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer src" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[CipherSpi](/Java/CipherSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CipherSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

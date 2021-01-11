---
title: SSLContextSpi.engineGetSocketFactory()
permalink: Java/SSLContextSpi/engineGetSocketFactory
date: 2021-01-11
key: JavaJava.S.SSLContextSpi
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLContextSpi.metodos valor="engineGetSocketFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract SSLSocketFactory engineGetSocketFactory()
~~~

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[SSLContextSpi](/Java/SSLContextSpi/)

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

---
title: KeyStoreSpi.engineProbe()
permalink: /Java/KeyStoreSpi/engineProbe/
date: 2021-01-11
key: Java.K.KeyStoreSpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineProbe" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean engineProbe(InputStream stream) throws IOException
~~~

## Parámetros
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[KeyStoreSpi](/Java/KeyStoreSpi/)

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

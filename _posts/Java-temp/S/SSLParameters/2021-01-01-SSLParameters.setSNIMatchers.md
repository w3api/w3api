---
title: SSLParameters.setSNIMatchers()
permalink: /Java/SSLParameters/setSNIMatchers/
date: 2021-01-11
key: Java.S.SSLParameters
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLParameters.metodos valor="setSNIMatchers" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setSNIMatchers(Collection<SNIMatcher> matchers)
~~~

## Parámetros
* **Collection&lt;SNIMatcher&gt; matchers**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<SNIMatcher> matchers" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SSLParameters](/Java/SSLParameters/)

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

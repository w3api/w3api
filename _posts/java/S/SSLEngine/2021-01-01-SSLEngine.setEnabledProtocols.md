---
title: SSLEngine.setEnabledProtocols()
permalink: Java/SSLEngine/setEnabledProtocols
date: 2021-01-11
key: JavaJava.S.SSLEngine
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLEngine.metodos valor="setEnabledProtocols" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setEnabledProtocols(String[] protocols)
~~~

## Parámetros
* **String[] protocols**,  {% include w3api/param_description.html metodo=_dato parametro="String[] protocols" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLEngine](/Java/SSLEngine/)

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

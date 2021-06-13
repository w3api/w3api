---
title: SSLEngine.setUseClientMode()
permalink: /Java/SSLEngine/setUseClientMode/
date: 2021-01-11
key: Java.S.SSLEngine
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLEngine.metodos valor="setUseClientMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setUseClientMode(boolean mode)
~~~

## Parámetros
* **boolean mode**,  {% include w3api/param_description.html metodo=_dato parametro="boolean mode" %}

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

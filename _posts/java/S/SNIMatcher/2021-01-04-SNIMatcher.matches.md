---
title: SNIMatcher.matches()
permalink: Java/SNIMatcher/matches
date: 2021-01-04
key: JavaJava.S.SNIMatcher
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SNIMatcher.metodos valor="matches" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract boolean matches(SNIServerName serverName)
~~~

## Parámetros
* **SNIServerName serverName**,  {% include w3api/param_description.html metodo=_data parametro="SNIServerName serverName" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SNIMatcher](/Java/SNIMatcher/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SNIMatcher.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

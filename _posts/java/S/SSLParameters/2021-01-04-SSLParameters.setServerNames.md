---
title: SSLParameters.setServerNames()
permalink: Java/SSLParameters/setServerNames
date: 2021-01-04
key: JavaJava.S.SSLParameters
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLParameters.metodos valor="setServerNames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setServerNames(List<SNIServerName> serverNames)
~~~

## Parámetros
* **List&lt;SNIServerName&gt; serverNames**,  {% include w3api/param_description.html metodo=_data parametro="List<SNIServerName> serverNames" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLParameters](/Java/SSLParameters/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLParameters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

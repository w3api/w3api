---
title: GSSContext.requestReplayDet()
permalink: Java/GSSContext/requestReplayDet
date: 2021-01-11
key: JavaJava.G.GSSContext
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSContext.metodos valor="requestReplayDet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void requestReplayDet(boolean state) throws GSSException
~~~

## Parámetros
* **boolean state**,  {% include w3api/param_description.html metodo=_dato parametro="boolean state" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[GSSContext](/Java/GSSContext/)

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

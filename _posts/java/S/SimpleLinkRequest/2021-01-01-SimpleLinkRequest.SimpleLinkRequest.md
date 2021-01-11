---
title: SimpleLinkRequest.SimpleLinkRequest()
permalink: Java/SimpleLinkRequest/SimpleLinkRequest
date: 2021-01-11
key: JavaJava.S.SimpleLinkRequest
category: java
tags: ['java se', 'jdk.dynalink.linker.support', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleLinkRequest.constructores valor="SimpleLinkRequest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleLinkRequest(CallSiteDescriptor callSiteDescriptor, boolean callSiteUnstable, Object... arguments)
~~~

## Parámetros
* **boolean callSiteUnstable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean callSiteUnstable" %}
* **CallSiteDescriptor callSiteDescriptor**,  {% include w3api/param_description.html metodo=_dato parametro="CallSiteDescriptor callSiteDescriptor" %}
* **Object... arguments**,  {% include w3api/param_description.html metodo=_dato parametro="Object... arguments" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SimpleLinkRequest](/Java/SimpleLinkRequest/)

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

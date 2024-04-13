---
title: LinkRequest.replaceArguments()
permalink: /Java/LinkRequest/replaceArguments/
date: 2021-01-11
key: Java.L.LinkRequest
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkRequest.metodos valor="replaceArguments" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LinkRequest replaceArguments(CallSiteDescriptor callSiteDescriptor, Object... arguments)
~~~

## Parámetros
* **CallSiteDescriptor callSiteDescriptor**,  {% include w3api/param_description.html metodo=_dato parametro="CallSiteDescriptor callSiteDescriptor" %}
* **Object... arguments**,  {% include w3api/param_description.html metodo=_dato parametro="Object... arguments" %}

## Clase Padre
[LinkRequest](/Java/LinkRequest/)

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

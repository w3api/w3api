---
title: RelinkableCallSite.relink()
permalink: /Java/RelinkableCallSite/relink/
date: 2021-01-11
key: Java.R.RelinkableCallSite
category: Java
tags: ['java se', 'jdk.dynalink', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RelinkableCallSite.metodos valor="relink" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void relink(GuardedInvocation guardedInvocation, MethodHandle relinkAndInvoke)
~~~

## Parámetros
* **GuardedInvocation guardedInvocation**,  {% include w3api/param_description.html metodo=_dato parametro="GuardedInvocation guardedInvocation" %}
* **MethodHandle relinkAndInvoke**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle relinkAndInvoke" %}

## Clase Padre
[RelinkableCallSite](/Java/RelinkableCallSite/)

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

---
title: GuardedInvocation.replaceMethods()
permalink: Java/GuardedInvocation/replaceMethods
date: 2021-01-11
key: JavaJava.G.GuardedInvocation
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardedInvocation.metodos valor="replaceMethods" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GuardedInvocation replaceMethods(MethodHandle newInvocation, MethodHandle newGuard)
~~~

## Parámetros
* **MethodHandle newGuard**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle newGuard" %}
* **MethodHandle newInvocation**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle newInvocation" %}

## Clase Padre
[GuardedInvocation](/Java/GuardedInvocation/)

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

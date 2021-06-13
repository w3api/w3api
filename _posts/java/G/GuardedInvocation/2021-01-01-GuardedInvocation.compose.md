---
title: GuardedInvocation.compose()
permalink: /Java/GuardedInvocation/compose/
date: 2021-01-11
key: Java.G.GuardedInvocation
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardedInvocation.metodos valor="compose" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodHandle compose(MethodHandle fallback)
public MethodHandle compose(MethodHandle guardFallback, MethodHandle switchpointFallback, MethodHandle catchFallback)
~~~

## Parámetros
* **MethodHandle fallback**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle fallback" %}
* **MethodHandle catchFallback**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle catchFallback" %}
* **MethodHandle guardFallback**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle guardFallback" %}
* **MethodHandle switchpointFallback**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle switchpointFallback" %}

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

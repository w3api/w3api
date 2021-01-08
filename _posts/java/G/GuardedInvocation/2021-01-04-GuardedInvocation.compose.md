---
title: GuardedInvocation.compose()
permalink: Java/GuardedInvocation/compose
date: 2021-01-04
key: JavaJava.G.GuardedInvocation
category: java
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
* **MethodHandle switchpointFallback**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle switchpointFallback" %}
* **MethodHandle catchFallback**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle catchFallback" %}
* **MethodHandle fallback**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle fallback" %}
* **MethodHandle guardFallback**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle guardFallback" %}

## Clase Padre
[GuardedInvocation](/Java/GuardedInvocation/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GuardedInvocation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

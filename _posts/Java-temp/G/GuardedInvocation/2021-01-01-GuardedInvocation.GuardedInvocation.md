---
title: GuardedInvocation.GuardedInvocation()
permalink: /Java/GuardedInvocation/GuardedInvocation/
date: 2021-01-11
key: Java.G.GuardedInvocation
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardedInvocation.constructores valor="GuardedInvocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GuardedInvocation(MethodHandle invocation)
public GuardedInvocation(MethodHandle invocation, MethodHandle guard)
public GuardedInvocation(MethodHandle invocation, MethodHandle guard, SwitchPoint switchPoint)
public GuardedInvocation(MethodHandle invocation, MethodHandle guard, SwitchPoint[] switchPoints, Class<? extends Throwable> exception)
public GuardedInvocation(MethodHandle invocation, MethodHandle guard, SwitchPoint switchPoint, Class<? extends Throwable> exception)
public GuardedInvocation(MethodHandle invocation, SwitchPoint switchPoint)
~~~

## Parámetros
* **SwitchPoint[] switchPoints**,  {% include w3api/param_description.html metodo=_dato parametro="SwitchPoint[] switchPoints" %}
* **Class&lt;? extends Throwable&gt; exception**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Throwable> exception" %}
* **MethodHandle invocation**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle invocation" %}
* **MethodHandle guard**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle guard" %}
* **SwitchPoint switchPoint**,  {% include w3api/param_description.html metodo=_dato parametro="SwitchPoint switchPoint" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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

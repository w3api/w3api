---
title: GuardedInvocation.GuardedInvocation()
permalink: Java/GuardedInvocation/GuardedInvocation
date: 2021-01-04
key: JavaJava.G.GuardedInvocation
category: java
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
* **SwitchPoint switchPoint**,  {% include w3api/param_description.html metodo=_data parametro="SwitchPoint switchPoint" %}
* **Class&lt;? extends Throwable&gt; exception**,  {% include w3api/param_description.html metodo=_data parametro="Class<? extends Throwable> exception" %}
* **MethodHandle guard**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle guard" %}
* **SwitchPoint[] switchPoints**,  {% include w3api/param_description.html metodo=_data parametro="SwitchPoint[] switchPoints" %}
* **MethodHandle invocation**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandle invocation" %}

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
{%- for _ldc in site.data.Java.G.GuardedInvocation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

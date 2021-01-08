---
title: SwingUtilities.invokeAndWait()
permalink: Java/SwingUtilities/invokeAndWait
date: 2021-01-04
key: JavaJava.S.SwingUtilities
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwingUtilities.metodos valor="invokeAndWait" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void invokeAndWait(Runnable doRun) throws InterruptedException, InvocationTargetException
~~~

## Parámetros
* **Runnable doRun**,  {% include w3api/param_description.html metodo=_data parametro="Runnable doRun" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [InvocationTargetException](/Java/InvocationTargetException/)

## Clase Padre
[SwingUtilities](/Java/SwingUtilities/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SwingUtilities.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

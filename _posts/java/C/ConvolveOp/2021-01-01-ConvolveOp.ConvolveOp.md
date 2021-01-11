---
title: ConvolveOp.ConvolveOp()
permalink: Java/ConvolveOp/ConvolveOp
date: 2021-01-11
key: JavaJava.C.ConvolveOp
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConvolveOp.constructores valor="ConvolveOp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ConvolveOp(Kernel kernel)
public ConvolveOp(Kernel kernel, int edgeCondition, RenderingHints hints)
~~~

## Parámetros
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_dato parametro="RenderingHints hints" %}
* **Kernel kernel**,  {% include w3api/param_description.html metodo=_dato parametro="Kernel kernel" %}
* **int edgeCondition**,  {% include w3api/param_description.html metodo=_dato parametro="int edgeCondition" %}

## Clase Padre
[ConvolveOp](/Java/ConvolveOp/)

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

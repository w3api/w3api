---
title: SynthLabelUI.paint()
permalink: /Java/SynthLabelUI/paint/
date: 2021-01-11
key: Java.S.SynthLabelUI
category: Java
tags: ['java se', 'javax.swing.plaf.synth', 'java.desktop', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SynthLabelUI.metodos valor="paint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void paint(Graphics g, JComponent c)
protected void paint(SynthContext context, Graphics g)
~~~

## Parámetros
* **SynthContext context**,  {% include w3api/param_description.html metodo=_dato parametro="SynthContext context" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}

## Clase Padre
[SynthLabelUI](/Java/SynthLabelUI/)

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

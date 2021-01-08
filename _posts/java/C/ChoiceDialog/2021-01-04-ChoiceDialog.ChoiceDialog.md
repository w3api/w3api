---
title: ChoiceDialog.ChoiceDialog()
permalink: Java/ChoiceDialog/ChoiceDialog
date: 2021-01-04
key: JavaJava.C.ChoiceDialog
category: java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceDialog.constructores valor="ChoiceDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ChoiceDialog()
public ChoiceDialog(T defaultChoice, Collection<T> choices)
public ChoiceDialog(T defaultChoice, T... choices)
~~~

## Parámetros
* **T... choices**,  {% include w3api/param_description.html metodo=_data parametro="T... choices" %}
* **T defaultChoice**,  {% include w3api/param_description.html metodo=_data parametro="T defaultChoice" %}
* **Collection&lt;T&gt; choices**,  {% include w3api/param_description.html metodo=_data parametro="Collection<T> choices" %}

## Clase Padre
[ChoiceDialog](/Java/ChoiceDialog/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChoiceDialog.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

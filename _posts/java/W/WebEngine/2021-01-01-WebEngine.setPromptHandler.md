---
title: WebEngine.setPromptHandler()
permalink: /Java/WebEngine/setPromptHandler/
date: 2021-01-11
key: Java.W.WebEngine
category: java
tags: ['java se', 'javafx.scene.web', 'javafx.web', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WebEngine.metodos valor="setPromptHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setPromptHandler(Callback<PromptData,String> handler)
~~~

## Parámetros
* **Callback&lt;PromptData**,  {% include w3api/param_description.html metodo=_dato parametro="Callback<PromptData" %}
* **String&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="String> handler" %}

## Clase Padre
[WebEngine](/Java/WebEngine/)

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
